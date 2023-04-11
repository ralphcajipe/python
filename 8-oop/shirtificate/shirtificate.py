# CS50 Shirtificate


from fpdf import FPDF


class Shirtificate:
    """An attempt to model a CS50 shirtificate."""

    def __init__(self, name):
        """Initialize name attribute."""
        self._name = name

    @classmethod
    def get_name(cls):
        """
        The is a class method that asks the user to input their name,
        and then it is stripping the name of any whitespace for clean input.

        :param cls: This is the class that the method is being called on
        :return: The name of the user.
        """
        name = input("Name: ").strip()
        return cls(name)

    def process_shirt(self):
        """This prints the name to the shirt."""

        # This is creating a pdf file with the orientation of portrait,
        # the unit of measurement is millimeters, and the format is A4.
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(False, 0)

        # This is the text that will be displayed on top as the title.
        pdf.set_font("Helvetica", size=48)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=62, border=0, align="C", txt="CS50 Shirtificate")

        # This displays the name of the person who is getting the shirt.
        pdf.ln()

        # Adding the image to the pdf.
        pdf.image("shirtificate.png", x=10, y=65, w=190)

        # This is the text that will be displayed on the shirt.
        pdf.set_font("Helvetica", size=24)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(w=0, h=120, border=0, align="C", txt=f"{self._name} took CS50")

        # Creating a pdf file called shirtificate.pdf.
        pdf.output("shirtificate.pdf")


def main():
    """
    Prompts the user for a name, and then processes the shirt with the
    name on it.
    """
    Shirtificate.get_name().process_shirt()
    print("Your shirtificate is ready! Check your directory.")


if __name__ == "__main__":
    main()
