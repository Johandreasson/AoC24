def dampen():
    if len(unsafe) == 1:
        report.remove(unsafe[0])
        unsafe.pop()
        return True

with open(r'C:\Users\JANDRE21\projects\.vscode\AoC24\2\input.txt', "r") as f:
    safe = 0
    for _ in range(1000):
        report = f.readline().split()
        report = [int(level) for level in report]

        dampened = False
        unsafe = []
        for i in range(len(report)-1):
            if abs(report[i] - report[i+1]) > 3 or report[i] == report[i+1]:
                unsafe.append(report[i+1])
        
        if not dampened:
            dampened = dampen()
        sorted_report = sorted(report)
        for i in range(len(report)):
            if report[i] == sorted_report[i] or report[i] == sorted_report[-i-1]:
                pass
            else:
                unsafe.append(report[i])
        if len(unsafe) > 0:
            print(report)
            print(unsafe, "\n")
        else:
            safe +=1

    print(safe)