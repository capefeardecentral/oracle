import os

import click
import openai

openai.api_key = os.getenv("OPEN_AI_KEY")
function_starters = {
    'python': 'def',
    'javascript': 'function',
    'elixir': 'def',
    'go': 'func',
    'solidity': 'function',
}

# better but still not good enough
# find a way to limit output to a single unit test
@click.command()
@click.option('--language', default='python', help='Language to use for code generation')
@click.argument('function')
def unit_test(language, function):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f'# {language}\n\n {function}\n\n # Unit test \n{function_starters[language]}',
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    test = response['choices'][0]['text']
    click.echo(test)

@click.command()
@click.argument('input')
def raw(input):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=input,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response['choices'][0]['text']
    click.echo(output)

