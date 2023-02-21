import os

import click
import openai

openai.api_key = os.getenv("OPEN_AI_KEY")

@click.command()
@click.argument('function')
def unit_test(function):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f'{function}\n\n # unit test',
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    test = response['choices'][0]['text']
    click.echo(test)

