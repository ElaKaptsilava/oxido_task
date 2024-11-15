import argparse
from html_article_generator.article_generator import ArticleHtmlGenerator


def main():
    parser = argparse.ArgumentParser(description="Generate an HTML article from a template.")
    parser.add_argument("-path", type=str, help="Name of the output template file", required=False)
    args = parser.parse_args()

    output_path = args.path

    if output_path:
        print(f"Output will be saved to: {output_path}")
        generator = ArticleHtmlGenerator(output_path=output_path)

    else:
        generator = ArticleHtmlGenerator()

    print("Starting the article generation process...")
    print(generator)
    generator.process_article()
    print("HTML article generated successfully!")


if __name__ == "__main__":
    main()
