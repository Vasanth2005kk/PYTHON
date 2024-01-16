regex_pattern =r"[.|,]"

import re
print("\n".join(re.split(regex_pattern, "100,000,000.000")))

#regex_pattern =r"\D" this use the is the all word in list in print it and number not removed

#regex_pattern =r",|\."

#regex_pattern =r"[,.]"