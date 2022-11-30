# mkdocs-changelog-plugin

**Warning** 还在开发中，很可能只有我一个人能用（x

一个用于在 mkdocs 文档中插入 changelog 时间轴的插件。

预览：https://note.tonycrane.cc/changelog/

## 安装
还在开发中，所以没有发布到 pypi，~~但你要想用我也不拦着~~，可以手动安装：

```shell
$ git clone https://github.com/TonyCrane/mkdocs-changelog-plugin.git
$ cd mkdocs-changelog-plugin
$ pip install . # or pip install -e .
```

## 使用
- 在 mkdocs.yml 中启用插件：
    ```yaml
    plugins:
        - changelog
    ```
- 在需要插入 changelog 的页面 meta 部分中添加：
    ```yaml
    changelog: True
    ```
- 然后在该页面需要插入 changelog 的地方添加：
    ```markdown
    {{changelog}}
    ```

具体的所有 changelog 要写在 docs/changelog.yml 中（默认，也可以通过 files 选项指定其它 yaml 文件位置）。具体格式有空再写，现在可以参考[我的 changelog.yml](https://github.com/TonyCrane/note/blob/master/docs/changelog.yml)。

## 开发
嘛，基本就是我用纯 html+css 糊出来自己用的，然后为了方便写了个插件，代码也比较乱，在别人的主题里面可能会~~格式混乱、颜色爆炸~~。有想修改、改进的我非常且热烈欢迎，尽管 PR 就好（

### TODO
虽然是老鸽子了，但还是象征性写一下接下来打算改进的内容：

- [ ] 在其它主题上测试并改进
- [ ] 支持分部分（？就是全堆一起感觉会太长了，可能分开来比较好，而且还更随意一点）
- [ ] 咕咕咕

## 参考
- [timvink/mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/)
- [unverbuggt/mkdocs-encryptcontent-plugin](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin)