class Statement:
    """The parent class for all statement types."""

    def __init__(self) -> None:
        self.statement_type = "Base Statement"
        self.data = None

    def get_statement_type(self):
        """Return statement_type."""
        return self.statement_type
    
    def set_statement_type(self, statement_type: str):
        """Set the statement type."""
        self.statement_type = statement_type

    def set_data(self, new_data):
        """Set the object's data with anything."""
        self.data = new_data

    def get_data(self):
        """Return the object's data."""
        return self.data


class PrintStatement(Statement):
    """Prints a string as a statement."""

    def __init__(self, print_string) -> None:
        super().__init__()

        self.set_statement_type("PrintStatement")
        self.set_data(print_string)
