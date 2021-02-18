class HTMLParser:
    def __init__(self, html_doc):
        self.html_doc = html_doc
        pass

    def set_html_doc(self, html_doc):
        self.html_doc = html_doc

    def find_first(self, output_arg, **finding_args):
        pass

    def find_all(self, n, output_arg, **finding_args):
        pass

    def find_parent(self, output_arg, **finding_args):
        pass

    def find_grandparent(self, n, output_arg, **finding_args):
        pass

    def remove_comment(self, **finding_args):
        pass

    def remove_all_comments(self):
        pass

    def remove_tag(self, **finding_args):
        pass
