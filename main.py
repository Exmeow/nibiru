# main.py

from textwrap import dedent


def define_env(env):
    @env.macro
    def aot_info(title, content):
        """
        生成《进击的巨人》风格的“现在可以公开的情报”卡片
        :param title: 标题 (如：超硬质钢)
        :param content: 正文内容
        """
        html = dedent(f"""
        <div class="aot-card">
            <div class="aot-header-label">现在可以公开的情报</div>
            <div class="aot-title">{title}</div>
            <div class="aot-separator"></div>
            <div class="aot-content">
                {content}
            </div>
        </div>
        """).strip()
        return html
