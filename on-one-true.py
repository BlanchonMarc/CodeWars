def only_one(*args, **kwargs):

    return (False if not args else True if args.count(True) == 1 else False)
