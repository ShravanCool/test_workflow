import sys
import re

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def get_migration_files(changed_files):
    migration_files = []
    for file_name in changed_files:
        if file_name.endswith('.pyc'):
            continue
        if "migrations" in file_name:
            migration_files.append(file_name)

    return migration_files

def check_add_not_null_column_without_default_value(file_contents):
    if re.search(".*migrations.AddField.*", file_contents) and re.search(".*AddDefaultValue.*", file_contents):
        return False
    elif re.search(".*migrations.AddField.*", file_contents):
        return True
    else:
        return False

def check_alter_column(file_contents):
    if re.search(".*migrations.AlterField.*", file_contents):
        return True
    return False

def check_drop_column(file_contents):
    if re.search(".*migrations.RemoveField.*", file_contents):
        return True
    return False

def check_drop_table(file_contents):
    if re.search(".*migrations.DeleteModel.*", file_contents):
        return True
    return False

def check_rename_column(file_contents):
    if re.search(".*migrations.RenameField.*", file_contents):
        return True
    return False

def check_rename_table(file_contents):
    if re.search(".*migrations.RenameModel.*", file_contents):
        return True
    return False

def check_unique_together_constraint(file_contents):
    if re.search(".*migrations.AlterUniqueTogether.*", file_contents):
        return True
    return False

def lint_migration_errors(file_contents):
    errors, warnings = [], []

    if check_add_not_null_column_without_default_value(file_contents):
        errors.append("NOT NULL Constraint on columns")

    if check_alter_column(file_contents):
        warnings.append("ALTERING columns (Could be backwards compatible, you may ignore this)")

    if check_drop_column(file_contents):
        errors.append("DROPPING columns")

    if check_drop_table(file_contents):
        errors.append("DROPPING table")

    if check_rename_column(file_contents):
        errors.append("RENAMING columns")

    if check_rename_table(file_contents):
        errors.append("RENAMING table")

    if check_unique_together_constraint(file_contents):
        errors.append("ADDING unique constraint")

    return errors, warnings

def main():
    num_args = len(sys.argv)
    changed_files = sys.argv[1:num_args]
    migration_files = get_migration_files(changed_files)
    all_errors = dict()
    all_warnings = dict()
    for migration_file in migration_files:
        file_contents = read_file(migration_file)
        errors, warnings = lint_migration_errors(file_contents)
        if len(errors):
            all_errors[migration_file] = errors
        if len(warnings):
            all_warnings[migration_file] = warnings
        
    print("Errors: ", all_errors)
    print("Warnings: ", all_warnings)

if __name__ == "__main__":
    main()
