from gpt.generate_persona import gpt4_generate_persona


class Persona:
    def __init__(self, name, age, gender, occupation, hobbies, wealth, health, belongings=None, religion=None, ethnicity=None):
        """
        Initializes a Persona instance with essential and descriptive attributes.

        Args:
            name (str): The name of the persona.
            age (int): Age of the persona.
            gender (str): Gender of the persona.
            occupation (str): Occupation or current status.
            hobbies (list): List of hobbies the persona enjoys.
            wealth (int): Wealth level (0 to 1000).
            health (int): Health level (0 to 100).
            belongings (list, optional): Persona's belongings. Defaults to None.
            religion (str, optional): Persona's religion. Defaults to None.
            ethnicity (str, optional): Persona's ethnicity. Defaults to None.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.hobbies = hobbies
        self.wealth = wealth
        self.health = health
        self.belongings = belongings
        self.religion = religion
        self.ethnicity = ethnicity

    @staticmethod
    def generate_persona_from_gpt(name: str):
        """
        Generates a Persona instance using GPT-generated data.

        Args:
            name (str): Name of the persona.

        Returns:
            Persona: An instance of the Persona class with GPT-generated attributes.
        """
        gpt_response = gpt4_generate_persona(name)
        return Persona(**gpt_response)

    def display_info(self):
        """Displays basic information about the persona."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")
        print(f"Hobbies: {', '.join(self.hobbies)}")
        print(f"Wealth: {self.wealth}")
        print(f"Health: {self.health}")
        print(f"Belongings: {', '.join(self.belongings) if self.belongings else 'None'}")
        print(f"Religion: {self.religion}")
        print(f"Ethnicity: {self.ethnicity}")

    def info_to_dict(self):
        """Returns a dictionary containing the persona's attributes."""
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "occupation": self.occupation,
            "hobbies": self.hobbies,
            "wealth": self.wealth,
            "health": self.health,
            "belongings": self.belongings,
            "religion": self.religion,
            "ethnicity": self.ethnicity,
        }

    def info_to_string_story(self):
        """
        Creates a string narrative describing the persona.

        Returns:
            str: Narrative description of the persona.
        """
        return (
            f"I am {self.name}. My age is {self.age}. My gender is {self.gender}. "
            f"My occupation is {self.occupation}. My hobbies are {', '.join(self.hobbies)}. "
            f"My wealth level is {self.wealth}. My health level is {self.health}. "
            f"My belongings are {', '.join(self.belongings) if self.belongings else 'None'}. "
            f"My religion is {self.religion}. My ethnicity is {self.ethnicity}."
        )

    def update_info(self, **kwargs):
        """
        Updates the persona's attributes with new values provided as keyword arguments.

        Args:
            **kwargs: Attribute names as keys and their new values as values.
                      Supported attributes: name, age, gender, occupation, hobbies,
                      wealth, health, belongings, religion, ethnicity.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
                print(f"Updated {key} to {value}")
            else:
                print(f"Attribute {key} not found in Persona.")
