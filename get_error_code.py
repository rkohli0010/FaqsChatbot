def extract_error_code(query) :
    error_codes = [
    "SYS001", "REP001", "POL001", "QRT001",
    "BUF001", "AUTH001", "CLC001", "MBP001"
    ]
    
    for code in error_codes :
      if code in query :
        return code

    return 'NoErrorCode'

