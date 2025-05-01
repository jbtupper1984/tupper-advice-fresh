class HomeOfficeWorkflow:
    def __init__(self):
        self.step = 0

    def next(self, input_text: str) -> str:
        if self.step == 0:
            self.step += 1
            return "Do you use a portion of your home exclusively for business? (yes/no)"
        elif self.step == 1:
            if "yes" in input_text.lower():
                self.step += 1
                return "Great. Do you know the square footage of your home office?"
            else:
                return "Home office deductions require exclusive use. This deduction may not apply to you."
        elif self.step == 2:
            self.step += 1
            return "Thanks. Based on your answers, it sounds like you qualify!"
        else:
            return "This workflow is complete!"
