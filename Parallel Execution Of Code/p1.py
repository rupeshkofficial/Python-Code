import subprocess

commands = [

       "echo Rupesh",
       "echo Aakraya",
       "echo Research"

        ]

processes = []

for command in commands:
    process =  subprocess.Popen(command, shell = True)
    processes.append(process)

for process in processes:
    process.wait()

print("All processes have finished.")