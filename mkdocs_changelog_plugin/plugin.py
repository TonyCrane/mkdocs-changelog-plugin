import os
import re

import yaml
from jinja2 import Template

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.utils import copy_file

from typing import Any, Dict

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = os.path.join(PLUGIN_DIR, "templates/changelog.html")

with open(TEMPLATE_DIR, "r", encoding="utf-8") as file:
    TEMPLATE = file.read()

class ChangelogPlugin(BasePlugin):
    config_scheme = (
        ("enabled", config_options.Type(bool, default=True)),
        ("file", config_options.Type(str, default="docs/changelog.yml")),
    )

    enabled = True

    def on_config(self, config: config_options.Config, **kwargs) -> Dict[str, Any]:
        if not self.enabled:
            return config
        
        if not self.config.get("enabled"):
            return config
        
        config["extra_css"] = ["css/timeline.css"] + config["extra_css"]
    
    def on_page_markdown(
        self, markdown: str, page: Page, config: config_options.Config, files, **kwargs
    ) -> str:
        if not self.enabled:
            return markdown
        
        if not self.config.get("enabled"):
            return markdown

        if not page.meta.get("changelog"):
            return markdown

        changelog_items = self._get_changelog_items()

        for placeholder, items in changelog_items.items():
            changelog = Template(TEMPLATE).render(items=items)
            markdown = re.sub(
                r"\{\{\s*%s\s*\}\}" % placeholder,
                changelog,
                markdown,
                flags=re.IGNORECASE,
            )

        return markdown

    def on_post_build(self, config: Dict[str, Any], **kwargs) -> None:
        if not self.enabled:
            return
        
        if not self.config.get("enabled"):
            return
        
        files = ["css/timeline.css"]
        for file in files:
            dest_file_path = os.path.join(config["site_dir"], file)
            src_file_path = os.path.join(PLUGIN_DIR, file)
            assert os.path.exists(src_file_path)
            copy_file(src_file_path, dest_file_path)
    
    def _get_changelog_items(self) -> dict:
        changelog_file = self.config.get("file")
        
        with open(changelog_file, "r", encoding="utf-8") as f:
            changelog_content = yaml.load(f, Loader=yaml.FullLoader)
        
        return self._produce_renderable_items(changelog_content)

    def _produce_renderable_items(self, changelog: list) -> dict:
        ret = dict()
        for part in changelog:
            placeholder = list(part.keys())[0]
            content = part[placeholder]
            items = []
            for _item in content:
                item = dict()
                item["time"] = list(_item.keys())[0]
                changes = []
                for _change in _item[item["time"]]:
                    change = dict()
                    change["type"] = list(_change.keys())[0]
                    change["content"] = _change[change["type"]]
                    changes.append(change)
                item["changes"] = changes
                items.append(item)
            ret[placeholder] = items
        return ret