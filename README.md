# Secure Password Generator

A simple Python-based password generator that creates secure, randomized passwords based on a user-defined length. 

## Features

*   **Customizable Length:** Users can specify the exact length of the password they want (minimum 8 characters).
*   **Guaranteed Complexity:** Every generated password is mathematically guaranteed to include:
    *   At least one digit (0-9)
    *   At least one letter (a-z, A-Z)
    *   At least one special character/punctuation mark
*   **Curated Character Set:** Automatically removes potentially confusing or problematic special characters (like quotes, brackets, and slashes) to ensure the generated passwords works easily across all platforms and databases.
*   **Continuous Validation:** The program repeatedly validates random combinations in the background until it finds one that satisfies all strict complexity requirements before presenting it to the user.


**Example Execution:**
```
Enter password length (minimum 8): 14
y7!mC@p9$Tz1#H
```

## How It Works Under the Hood

1. **Character Pools**: The script establishes global pools of `string.ascii_letters`, integers from `0` to `9`, and `string.punctuation`.
2. **Sanitization**: It strips out tricky symbols `['"',',','.','/','|','[',']','{','}','~','`','=','>','<',';',':','?','\\']` from the available pool.
3. **Generation Loop**: It picks a random symbol from the sanitized pool `length` times.
4. **Validation Check**: The custom `f(password)` function iterates through the generated string to trigger boolean flags for each required character type. If a character type is missing, the candidate password is trashed and the script tries again until a perfect candidate is created.

