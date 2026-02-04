### 96
print("\n===== 96 ======\n")

error_and_info_list = "INFO: Server started\nINFO: OK\nERROR: Fail\nINFO: User logged in\nERROR: High memory usage\nINFO: OK\nERROR: Database connection lost\nINFO: Server shutdown"

with open("server.log", "w") as f:
    f.write(error_and_info_list)

with open("server.log", "r") as f:
    content = f.readlines()

error_count = 0

for line in content:
    if "ERROR" in line:
        error_count += 1
    else:
        continue
print('Number of "ERROR" lines that exist: ', error_count)
