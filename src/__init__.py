# dummy python module

def main():
    """Really long line that should not be annotated as we're overwriting max line-length with a custom .ini file."""
    print ("hello")


class bad_class_name:
    # pep8-naming should complain about this
    pass


if __name__  == "__main__":
    main()
