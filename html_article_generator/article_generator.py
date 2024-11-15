import typing

import openai
from openai import OpenAI

from .setup import PROMPT_PATH, ARTICLE_PATH, OPENAI_API_KEY, OUTPUT_PATH


class ArticleHtmlGenerator:
    def __init__(self, open_ai_key: str = OPENAI_API_KEY, article_path: str = ARTICLE_PATH,
                 output_path: str = OUTPUT_PATH,
                 prompt_path: str = PROMPT_PATH) -> None:
        self.open_ai_key = open_ai_key
        self.article_path = article_path
        self.output_path = output_path
        self.prompt_path = prompt_path
        openai.api_key = self.open_ai_key

    def __repr__(self):
        return f"ArticleHtmlGenerator(article_path={self.article_path}, output_path={self.output_path}, prompt_path={self.prompt_path})"

    def read_article(self) -> typing.Union[str, None]:
        try:
            with open(self.article_path, "r", encoding="utf-8") as article:
                article_text = article.read()
            return article_text
        except FileNotFoundError:
            print(f"Article file not found: {self.article_path}")
            return None

    def read_prompt(self) -> typing.Union[str, None]:
        try:
            with open(self.prompt_path, "r", encoding="utf-8") as prompt:
                prompt_text = prompt.read()
            return prompt_text
        except FileNotFoundError:
            print(f"Prompt file not found: {self.prompt_path}")
            return None

    def generate_html(self, article_text: str) -> typing.Union[str, None]:
        prompt = self.read_prompt() + article_text
        if prompt:
            try:
                client = OpenAI()
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "user", "content": prompt},
                    ],
                )
                print(completion.choices[0].message.content[1:-1])
                return completion.choices[0].message.content
            except Exception as exception:
                print(f"Error when generating html: {exception}")
        return None

    def save_html(self, html_content: str) -> None:
        try:
            with open(self.output_path, "w", encoding="utf-8") as file:
                file.write(html_content)
        except IOError:
            print(f"Error when saving html: {self.output_path}")

    def process_article(self) -> None:
        article_text = self.read_article()
        if article_text:
            html_content = self.generate_html(article_text).strip("```html").strip("```").strip()
            if html_content:
                self.save_html(html_content)
