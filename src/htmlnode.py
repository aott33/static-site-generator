class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This feature is not yet implemented.")

    def props_to_html(self):
        html = ''
        if not self.props:
            return html

        for key,value in self.props.items():
            html += f' {key}="{value}"'
        
        return html    
    
    def __repr__(self):
        html_node_str = f'''
        tag: {self.tag}
        value: {self.value}
        children: {self.children}
        props: {self.props}
        '''
        return html_node_str
