# mkdocs-changelog-plugin

一个用于在 mkdocs 文档中插入 changelog 时间轴的插件。

预览：https://note.tonycrane.cc/changelog/

## 安装
可以通过 pypi 直接安装：
```shell
$ pip install mkdocs-changelog-plugin
```

也可以从源码安装

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
- changelog 从外部的 yaml 文件读取，默认在 docs/changelog.yml 中，可以通过 file 选项来选择其他位置：
    ```yaml
    plugins:
      - changelog:
          file: changelog.yml
    ```
- 按照格式编写 changelog yaml 文件（见下）
- 在需要插入 changelog 的页面 meta 部分中添加：
    ```yaml
    changelog: True
    ```
- 在页面需要插入对应部分的位置添加：
    ```markdown
    {{ placeholder }}
    ```

### changelog.yml 格式
例如：
```yaml
- "placeholder1":
  - "time1":
    - "type": text
    - "type": text
- "placeholder":
  - "time2":
    - "type":
        text: text
        href: /link/to/page/
    - "type":
        text: text
        href: /link/to/page/
  - "time3":
    - "type": text
```

- placeholder 是在 md 文件插入位置写入 {{ }} 的内容
- time 是时间标题
- type 是更改类型
    - 插件内自带三种：
        - newpage：新建页面
        - pageupdate：页面更新
        - function：功能性更新
    - 可以自定义
        - 插入 custom css 即可，例如自定义 refactor type：
            ```css
            .changelog-type-refactor {
                background-color: #c63f94b0;
            }
            .changelog-type-refactor::before {
                content: "文档重构";
            }
            ```
        - 如果没有对应 css，则显示为蓝色的“更新”
- type 后可以直接写文本，会直接写在更新类型后面（不支持 markdown，但可以 html）
- type 后也可以按如上写 text 和 href，此时会给 text 加上 href 指定的 link（利用 a 元素）

具体可以参考[我的 changelog.yml](https://github.com/TonyCrane/note/blob/master/docs/changelog.yml)。

### 主题适配
感觉 mkdocs 主流主题只有 material 用得多了，所以没做其他主题的适配。基本上就差在几个颜色的问题上，问题不大，可以自己通过 css 来覆盖这里规定的颜色，具体看 css/timeline.css。

## 开发
嘛，基本就是我用纯 html+css 糊出来自己用的，然后为了方便写了个插件，代码也比较乱，在别人的主题里面可能会~~格式混乱、颜色爆炸~~。有想修改、改进的我非常且热烈欢迎，尽管 PR 就好（

## 参考
- [timvink/mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/)
- [unverbuggt/mkdocs-encryptcontent-plugin](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin)