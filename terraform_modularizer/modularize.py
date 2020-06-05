from terraform_modularizer.terraform_modularizer import parseargs, modularize
from terraform_modularizer.help_messages import help_messages

if __name__ == '__main__':
    args = parseargs()
    try:
        modularize(args.resources_file, args.module)
    except FileNotFoundError:
        print(help_messages['no_cli'])
