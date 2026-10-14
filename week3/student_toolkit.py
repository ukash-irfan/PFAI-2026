def parse_marks(text):
    """Convert comma-separated text into a validated list of marks."""   
    if not text.strip():       
        raise ValueError("Enter at least one mark.")    
    parts = text.split(",")   
    marks = []    
    for part in parts:     
            if not part.strip():    
                raise ValueError("A mark is missing between commas.")    
            mark = float(part.strip())       
            if mark < 0 or mark > 100:       
                raise ValueError("Every mark must be between 0 and 100.")     
                marks.append(mark)      
                return marks 