from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Error: parent node doesn't have a tag")

        if self.children == None:
            return ValueError("Error: parent node doesn't have children")
        
        html_string = f'<{self.tag}' 
              
        if self.props:
            html_string += self.props_to_html()

        html_string += '>'
        
        if self.children:
            for child in self.children:
                html_string += child.to_html()
        
        html_string += f'</{self.tag}>'

        return html_string
