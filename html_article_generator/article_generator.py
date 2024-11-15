import typing

import openai
from openai import OpenAI

from .setup import PROMPT_PATH, ARTICLE_PATH, OPENAI_API_KEY, OUTPUT_PATH


class ArticleHtmlGenerator:
    def __init__(self, open_ai_key: str = OPENAI_API_KEY, article_path: str = ARTICLE_PATH,
                 output_path: str = OUTPUT_PATH, prompt_path: str = PROMPT_PATH) -> None:
        """
        Initializes the ArticleHtmlGenerator with the provided paths and OpenAI API key.

        :param open_ai_key: The OpenAI API key.
        :param article_path: The file path to the article to be processed.
        :param output_path: The file path where the generated HTML will be saved.
        :param prompt_path: The file path for the prompt to prepend to the article text.
        """
        self.open_ai_key = open_ai_key
        self.article_path = article_path
        self.output_path = output_path
        self.prompt_path = prompt_path
        openai.api_key = self.open_ai_key

    def __repr__(self) -> str:
        """
        Returns a string representation of the ArticleHtmlGenerator instance.

        :return: A formatted string with the article and output paths.
        """
        return f"ArticleHtmlGenerator(article_path={self.article_path}, output_path={self.output_path}, prompt_path={self.prompt_path})"

    def _read_file(self, file_path: str) -> typing.Union[str, None]:
        """
        Reads the contents of a file and returns the text, or None if an error occurs.

        :param file_path: Path to the file to read.
        :return: The contents of the file or None if the file could not be read.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
        return None

    def read_prompt(self) -> typing.Optional[str]:
        """
        Reads the prompt content from the specified file.

        :return: Prompt text or None if the file is not found or cannot be read.
        """
        return self._read_file(self.prompt_path)

    def generate_html(self, article_text: str) -> typing.Optional[str]:
        """
        Generates HTML content by combining the prompt and the article text and sending it to OpenAI for processing.

        :param article_text: The article content to be included in the HTML generation.
        :return: The generated HTML content or None if generation fails.
        """
        prompt = self.read_prompt() + article_text if self.read_prompt() else article_text
        if prompt:
            try:
                client = OpenAI()
                completion = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                )
                generated_content = completion.choices[0].message.content.strip("```html").strip("```").strip()
                print(generated_content)
                return generated_content
            except Exception as e:
                print(f"Error generating HTML: {e}")
        return None

    def save_html(self, html_content: str) -> None:
        """
        Saves the generated HTML content to the specified output file.

        :param html_content: The HTML content to be saved.
        """
        try:
            with open(self.output_path, "w", encoding="utf-8") as file:
                file.write(html_content)
        except IOError as e:
            print(f"Error saving HTML to {self.output_path}: {e}")

    def process_article(self) -> None:
        """
        Processes the article by reading its content, generating HTML, and saving the result.
        """
        article_text = self._read_file(self.article_path)
        if article_text:
            html_content = self.generate_html(article_text)
            if html_content:
                self.save_html(html_content)
            else:
                print("Failed to generate HTML content.")
        else:
            print("Failed to read the article.")
