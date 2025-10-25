def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "command_parts":
        return
    source_file, source_file = command_parts[1], command_parts[2]
    if source_file == source_file:
        return
    try:
        with open(source_file, "r") as file_in, open(source_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
