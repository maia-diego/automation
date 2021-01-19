import os

dir = r'C:\IBM\Treinamentos\WebApp_Flask\log'
path_testrunner = r'"C:\Program Files\SmartBear\SoapUI-5.6.0\bin\testrunner.bat"'
path_soap_project = r'C:\IBM\Treinamentos\WebApp_Flask\soap\automation-TestCorreios-soapui-project.xml'


def clear_dir(cep):
    logs = os.listdir(dir)
    length_logs = len(logs)
    del_files = 0

    for log in logs:
        if log.endswith(".txt"):
            try:
                os.remove(dir + "\\" + log)
            except OSError as e:
                print(e)
            else:
                del_files += 1

    if del_files == length_logs:
        print("Directory is cleared successfully")
    else:
        print("Some files have not been deleted")
    val = run_test(cep)
    return val


def run_test(cep):
    # command = "C:\\Users\\DiegoDeFreitasMaia\\Documents\\TreinamentoAutomacao\\Projeto\\TestRunner\\run.vbs"
    command = 'call ' + path_testrunner + ' -Gcep=' + cep + ' -r -a -f' + dir + ' ' + path_soap_project
    print(command)
    try:
        print("Running tests...")
        os.system(command)
    except OSError as e:
        print(e)

    v = validation_test(dir)
    return v


def validation_test(path):
    logs = os.listdir(path)
    length_logs = len(logs)
    validation = {}

    for log in logs:
        if 'tc001' in log:
            key = 'Web Service Search CEP'
            if 'OK' in log:
                validation[key] = "Passed"
            elif 'UNKNOWN' in log:
                validation[key] = "Missing Assertion"
            else:
                validation[key] = "Failed"
        elif 'tc002' in log:
            key = 'Web Service Blank Input Check'
            if 'OK' in log:
                validation[key] = "Passed"
            elif 'UNKNOWN' in log:
                validation[key] = "Missing Assertion"
            else:
                validation[key] = "Failed"
        elif 'tc003' in log:
            key = 'Web Service Search CEP with Dash'
            if 'OK' in log:
                validation[key] = "Passed"
            elif 'UNKNOWN' in log:
                validation[key] = "Missing Assertion"
            else:
                validation[key] = "Failed"
        elif 'tc004' in log:
            key = 'Web Service Invalid Input Check'
            if 'OK' in log:
                validation[key] = "Passed"
            elif 'UNKNOWN' in log:
                validation[key] = "Missing Assertion"
            else:
                validation[key] = "Failed"
        elif 'tc005' in log:
            key = 'Known Typed CEP'
            if 'OK' in log:
                validation[key] = "Failed"
            elif 'UNKNOWN' in log:
                validation[key] = "Missing Assertion"
            else:
                validation[key] = "Passed"
        elif 'tc006' in log:
            key = 'Valid Typed CEP'
            if 'OK' in log:
                validation[key] = "Failed"
            elif 'UNKNOWN' in log:
                validation[key] = "Missing Assertion"
            else:
                validation[key] = "Passed"

    return validation




