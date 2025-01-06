import re

multiply = [0];

with open("MulList.txt") as f:
    lines = f.readlines();
    data = "".join(l.rstrip() for l in lines)
    
    data = re.split("don't\(\)", data);

    for i in range(len(data)):
        do_lines = re.split("do\(\)", data[i]);

        if i != 0:
            do_lines = do_lines[1:];

        for run in do_lines:
            parsed_muls = re.findall(r'mul\(\d+,\d+\)', run);

            for mul_pairs in parsed_muls:
                run2 = mul_pairs.replace('mul(', '').replace(')', '');
                val1, val2 = run2.split(",");
                multiply.append(float(val1)*float(val2));
        
print(sum(multiply))
# 167650499
# 95846796