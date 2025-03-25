class CodeBuilder:
    def __init__(self, root_name):
        self._root = root_name
        self.fields = {}

    def add_field(self, type, name):
        self.fields[type]=name
        return self

    def __str__(self):
        lines = []
        lines.append(f"class {self._root}:")
        indent_size = "  "
        indent = indent_size * 1
        if len(self.fields)>0:
            lines.append(indent+"def __init__(self):")
        else:
            lines.append(indent+"pass")
        indent = indent_size * 2
        for key,value in self.fields.items():
            lines.append(indent+f"self.{key} = {value}")
        return "\n".join(lines)

if __name__=="__main__":
    cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
    print(cb)