import subprocess
from sys import exit


def signal_handler(sig, frame):
    exit(0)


SPECIAL_CHARACTERS = ["\u2826", "\u280B", "\u2819", "\u2839", "\u2838", "\u283C",
                      "\u2827", "\u280F", "\u2839", "\u2838", "\u283C", "\u2834", "\u2807", "\u280F"]


def remove_special_characters(text):
    for char in SPECIAL_CHARACTERS:
        text = text.replace(char, "")
    return text


def execute_command(command):
    # run command as global subprocess (that can be stopped at any time with signal_handler)
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # read from process and print real-time output to python shell
    result = []
    while True:
        output = process.stdout.readline()
        if not output and process.poll() is not None:
            break
        output = remove_special_characters(output).strip()
        if output:
            result.append(output)

    # wait until process finishes
    return_code = process.wait()
    answer = " ".join(result)
    if return_code == 0:
        return answer

    # else
    print(f"return code: {return_code}")
    return f"error: {return_code}"


def run_llama2(prompt):
    command = (fr'ollama run llama2 "{prompt}"')
    return execute_command(command)


def summarize(content):
    prompt = "Summarize the following text, listing the 3 most important points. Example format 1. xxx , 2. xxx, 3. xxx"
    prompt += content
    result = run_llama2(prompt)
    print(result)
    return result
