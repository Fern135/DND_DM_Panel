# max
import openai
# from ...conf.config.config import op_ai
from ...conf.config.config import op_ai

# Low Temperature: Lowest Possible Value (0.0): deterministic and focused outputs

# Low, but not Extreme (e.g., 0.1 - 0.5): focused and deterministic, 
                                            # but with a bit more randomness 
                                            #than at the lowest temperature.

# High Temperature:
# Moderately High (e.g., 0.8): The output becomes more diverse and creative. aka more creative

# Highest Possible Value (1.0):
#   The model is highly exploratory and generates very diverse outputs.
#   It may produce more unexpected and unconventional text.
#   The generated text is likely to be more random and less constrained by typical language patterns.


class Max:
    def __init__(self) -> None:
        openai.api_key = op_ai
        self.token = 150
        
    def setPrompt(self, Prompt=None):
        if Prompt is not None:
            self.Prompt = Prompt
        return self

    def chat(self, prompt=None):
        if prompt is not None and self.Prompt is None:
            openai.Completion.create(
                engine="text-davinci-002",  # or another available engine
                prompt=prompt,
                max_tokens=self.token  # Adjust as needed
            ).choices[0].text.strip()

        return self

# Example usage
user_input = "What is the meaning of life?"
mx = Max()
chat_response = mx.setPrompt(input).chat()
print(chat_response)
