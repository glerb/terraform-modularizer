help_messages = {
    "parser_description": "Moves Terraform state for existing, specified AWS resources from the root module to a child module, preventing the destroy/recreate cycle after moving the Terraform code for these resources to a child module path. The underlying interface is the Terraform CLI, executed in an OS subprocess. The easiest way to use this script is to move the Terraform code for the resources to a single file located in the module path and run the script on that file. 'terraform plan' will not generate a diff on the resources that moved to the module.",
    "resources_help": "The Terraform file that contains all the AWS resources to be moved to the child module.",
    "module_help": "The name of the child module to which the AWS resources will be moved. Do not include leading or trailing slashes. {0}**Warning!**{1} The underlying 'terraform state mv' command will silently create a module with this name in the state file if it doesn't exist. If you intend to move resources to an existing module, type the module name carefully!",
    "no_terraform": "The Terraform file '{0}' doesn't exist.",
    "invalid_terraform": "Are you sure you specified a valid Terraform HCL file? There don't seem to be any valid AWS resources in it.",
    "no_cli": "It appears that the Terraform CLI is not installed on this system, or is not in the PATH of the shell environment.",
}
