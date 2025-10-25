def copy_file(command: str) -> None:
    cp = command.split()
    if len(cp) != 3 or cp[0] != "cp":
        return
    source, dest = cp[1], cp[2]
    if source == dest:
        return
    try:
        with open(source, "r") as file_in, open(dest, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
