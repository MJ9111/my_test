import json

def parse_results():
    with open('results.txt', 'r') as file:
        lines = file.readlines()
    results = []
    for line in lines:
        if 'FAILED' in line:
            test_name = line.split('::')[1]
            results.append({"test": test_name, "result": "failed"})
        elif 'PASSED' in line:
            test_name = line.split('::')[1]
            results.append({"test": test_name, "result": "passed"})
    return results

results = parse_results()
print(json.dumps(results))
