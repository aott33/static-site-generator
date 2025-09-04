from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node doesn't have a value")

        if self.tag == None:
            return self.value
        
        html_string = f'<{self.tag}' 
        props_html = ''
        if self.props:
            html_string += self.props_to_html()

        html_string += f'>{self.value}</{self.tag}>'

        return html_string
