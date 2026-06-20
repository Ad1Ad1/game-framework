import os
import argparse
import shutil
import inspect
import models
import program
import data
import warnings

def main():
    datapath, programpath, modelspath=inspect.getfile(data), inspect.getfile(program), inspect.getfile(models)

    working_dir=os.getcwd()

    parser=argparse.ArgumentParser(description="Manage framework")
    subparsers = parser.add_subparsers(dest='function', required=True, help="function to execute")
    subparsers.add_parser('view_models_packs')

    register_parser = subparsers.add_parser('register_models_pack')
    register_parser.add_argument('name', type=str, help="name of pack to register")
    register_parser.add_argument("-f", "--folder",help="folder where to execute function")

    delete_parser=subparsers.add_parser('delete_models_pack')
    delete_parser.add_argument('name', type=str, help="name of pack to delete")
    delete_parser.add_argument("-f", "--folder",help="folder where to execute function")

    project_parser = subparsers.add_parser('project')
    project_subparsers = project_parser.add_subparsers(dest='project_function', required=True, help="project function to execute")

    create_parser = project_subparsers.add_parser('create')
    create_parser.add_argument('name', type=str, help="name of project to create")
    create_parser.add_argument("-f", "--folder",help="folder where to execute function")
    create_parser.add_argument("-n", "--requirementfilename",help="custom requirement file name")

    add_requirement_parser=project_subparsers.add_parser("add_requirement")
    add_requirement_parser.add_argument('name', type=str, help="name of requirement to add")
    add_requirement_parser.add_argument("-f", "--folder",help="folder where to execute function")
    add_requirement_parser.add_argument("-n", "--requirementfilename",help="custom requirement file name")

    delete_requirement_parser=project_subparsers.add_parser("delete_requirement")
    delete_requirement_parser.add_argument('name', type=str, help="name of requirement to delete")
    delete_requirement_parser.add_argument("-f", "--folder",help="folder where to execute function")
    delete_requirement_parser.add_argument("-n", "--requirementfilename",help="custom requirement file name")
    delete_requirement_parser.add_argument("-a", "--deleteallrequirements",help="marker if delete all file requirements")

    import_requirement_parser=project_subparsers.add_parser("import_requirements")
    import_requirement_parser.add_argument("-n", "--requirementfilename",help="custom requirement file name")
    import_requirement_parser.add_argument("-i", "--ignore",help="ignore warnings(any except e) or display errors(e)")

    import_requirement_parser=project_subparsers.add_parser("view_requirements")
    import_requirement_parser.add_argument("-n", "--requirementfilename",help="custom requirement file name")

    args = parser.parse_args()

    try:
        if args.folder:
            working_dir=os.path.join(working_dir, args.folder)
    except:
        pass

    library_dir = os.path.dirname(os.path.abspath(__file__))
    requirements=data.Database(os.path.join(library_dir, "models_requirements.json"), "FRAMEWORK MANAGER", sinit=True)
    if requirements.retrieve("", total=True)=="ERR":
        requirements.new()
        REQUIREMENTS={}
    else:
        REQUIREMENTS=requirements.retrieve("", total=True)

    if args.function=="register_models_pack":
        file=os.path.join(working_dir, f"{args.name}.py")
        if os.path.isfile(file):
            if requirements.retrieve(args.name)!="ERR":
                parser.error(f"A models pack with name {args.name} already exists")
            else:
                requirements.change(args.name,[file, f"{args.name}.py"])
        else:
            parser.error(f"The file {args.name}.py does not exist at that path. Please check the correctness of path")

    elif args.function=="delete_models_pack":
        if requirements.retrieve(args.name)!="ERR":
            requirements.delete(args.name)
        else:
            parser.error(f"A models pack with name {args.name} does not exist")

    elif args.function=="view_models_packs":
        print("=================")
        for requirement in REQUIREMENTS:
            print(requirement)
        print("=================")
        
    elif args.function=="project":
        req_fn="models_requirements.json" if not args.requirementfilename else args.requirementfilename
        if args.project_function=="create":
            os.makedirs(os.path.join(working_dir, args.name),exist_ok=True)
            project_requirements=data.Database(os.path.join(working_dir, args.name, req_fn), "FRAMEWORK MANAGER", sinit=True)
            project_requirements.new()
            shutil.copy(modelspath, os.path.join(working_dir, args.name, "models.py"))
            shutil.copy(datapath, os.path.join(working_dir, args.name, "data.py"))
            shutil.copy(programpath, os.path.join(working_dir, args.name, "program.py"))
        else:
            project_requirements=data.Database(os.path.join(working_dir, req_fn), "FRAMEWORK MANAGER", sinit=True)
        if args.project_function=="add_requirement":
            if args.name in REQUIREMENTS:
                if args.name in project_requirements.retrieve("",total=True):
                    parser.error(f"A models pack with name {args.name} is already in project requirements")
                else:
                    project_requirements.change(args.name, 0)
            else:
                parser.error(f"A models pack with name {args.name} does not exist")

        elif args.project_function=="delete_requirement":
            if args.deleteallrequirements or args.deleteallrequirements==0:
                project_requirements.delete("", total=True)
            else:
                if args.name in project_requirements.retrieve("",total=True):
                    project_requirements.delete(args.name)
                else:
                    parser.error(f"A models pack with name {args.name} does not exist in project requirements")

        elif args.project_function=="import_requirements":
            for requirement in project_requirements.retrieve("",total=True):
                if requirement in REQUIREMENTS:
                    shutil.copy(REQUIREMENTS[requirement][0], os.path.join(working_dir, REQUIREMENTS[requirement][1]))
                else:
                    if args.ignore=="e":
                        parser.error(f"A models pack with name {requirement} does not exist")
                    elif args.ignore or args.ignore==0:
                        pass
                    else:
                        warnings.warn(f"A models pack with name {requirement} does not exist, skipping this requirement")

        elif args.project_function=="view_requirements":
            print("=================")
            for requirement in project_requirements.retrieve("",total=True):
                print(requirement)
            print("=================")
            
if __name__ == "__main__":
    main()
