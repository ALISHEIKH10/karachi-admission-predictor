"""
Karachi Universities Data
Complete information about major universities in Karachi
"""

KARACHI_UNIVERSITIES = {
    "DUET": {
        "full_name": "Dawood University of Engineering and Technology",
        "type": "Public",
        "location": "New M.A. Jinnah Road, Karachi",
        "established": 1962,
        "website": "www.duet.edu.pk",
        "phone": "021-99261261",
        "fields": ["Engineering", "Technology"],
        "programs": ["BS Electrical Engineering", "BS Mechanical Engineering", 
                    "BS Civil Engineering", "BS Computer Science",
                    "BS Chemical Engineering", "BS Industrial Engineering",
                    "BS Textile Engineering", "BS Metallurgical Engineering"],
        "entry_test": "DUET Entry Test",
        "test_marks": 100,
        "merit_formula": "Matric 10% + Inter 40% + Entry Test 50%",
        "min_inter_marks": 60,  # Percentage
        "annual_fee": 75000,
        "ranking": 1,
        "strengths": [
            "Best public engineering university in Karachi",
            "Very low fee — affordable for all",
            "Strong industry connections",
            "Experienced faculty",
            "Good lab facilities"
        ],
        "weaknesses": [
            "Limited programs (Engineering only)",
            "Older infrastructure in some departments",
            "Less extracurricular activities"
        ],
        "environment": "Professional and focused",
        "campus_life": "Medium",
        "job_placement": "Excellent",
        "rating": 4.2,
        "merit_2024": {
            "Electrical Engineering": 78,
            "Mechanical Engineering": 75,
            "Civil Engineering": 72,
            "Computer Science": 80,
            "Chemical Engineering": 70,
        }
    },
    
    "NED": {
        "full_name": "NED University of Engineering and Technology",
        "type": "Public",
        "location": "University Road, Karachi",
        "established": 1922,
        "website": "www.neduet.edu.pk",
        "phone": "021-99261261",
        "fields": ["Engineering", "Technology", "Architecture"],
        "programs": ["BS Electrical Engineering", "BS Mechanical Engineering",
                    "BS Civil Engineering", "BS Computer & Information Systems",
                    "BS Chemical Engineering", "BS Architecture",
                    "BS Biomedical Engineering", "BS Petroleum Engineering"],
        "entry_test": "NED Entry Test",
        "test_marks": 100,
        "merit_formula": "Matric 10% + Inter 40% + Entry Test 50%",
        "min_inter_marks": 65,
        "annual_fee": 55000,
        "ranking": 1,
        "strengths": [
            "Oldest & most prestigious engineering university in Karachi",
            "Excellent alumni network",
            "Best job placements in Karachi",
            "Strong research culture",
            "HEC recognized top university"
        ],
        "weaknesses": [
            "Very competitive admission",
            "High workload",
            "Limited seats available"
        ],
        "environment": "Highly academic and competitive",
        "campus_life": "Active",
        "job_placement": "Excellent",
        "rating": 4.5,
        "merit_2024": {
            "Electrical Engineering": 85,
            "Mechanical Engineering": 82,
            "Civil Engineering": 78,
            "Computer & Information Systems": 87,
            "Chemical Engineering": 75,
            "Architecture": 80,
        }
    },
    
    "UBIT_KU": {
        "full_name": "University of Karachi — UBIT",
        "type": "Public",
        "location": "University Road, Karachi",
        "established": 1951,
        "website": "www.uok.edu.pk",
        "phone": "021-99261300",
        "fields": ["IT", "Computer Science", "Sciences", "Arts", "Commerce", "Law"],
        "programs": ["BS Computer Science", "BS Information Technology",
                    "BS Software Engineering", "BS Commerce", "BS Economics",
                    "BS Physics", "BS Chemistry", "BS Mathematics",
                    "LLB Law", "BS Psychology", "BS Mass Communication"],
        "entry_test": "KU Entry Test",
        "test_marks": 100,
        "merit_formula": "Inter 50% + Entry Test 50%",
        "min_inter_marks": 55,
        "annual_fee": 95000,
        "ranking": 2,
        "strengths": [
            "Largest university in Karachi",
            "Widest range of programs",
            "Very affordable fee",
            "Strong research departments",
            "Beautiful large campus"
        ],
        "weaknesses": [
            "Large class sizes",
            "Some departments need improvement",
            "Parking and transport issues"
        ],
        "environment": "Diverse and vibrant",
        "campus_life": "Very Active",
        "job_placement": "Good",
        "rating": 3.8,
        "merit_2024": {
            "Computer Science": 75,
            "Information Technology": 70,
            "Software Engineering": 73,
            "Commerce": 65,
            "Economics": 68,
        }
    },
    
    "IBA": {
        "full_name": "Institute of Business Administration",
        "type": "Public",
        "location": "Garden/City Campus, Karachi",
        "established": 1955,
        "website": "www.iba.edu.pk",
        "phone": "021-38103000",
        "fields": ["Business", "Computer Science", "Economics", "Social Sciences"],
        "programs": ["BBA", "BS Computer Science", "BS Economics",
                    "BS Accounting & Finance", "BS Social Sciences",
                    "BS Mathematical Sciences", "BS Entrepreneurship"],
        "entry_test": "IBA Aptitude Test (SAT-like)",
        "test_marks": 100,
        "merit_formula": "Inter 30% + IBA Test 50% + Interview 20%",
        "min_inter_marks": 70,
        "annual_fee": 480000,
        "ranking": 1,
        "strengths": [
            "Top business school in Pakistan",
            "Best BBA/MBA in Karachi",
            "Excellent corporate connections",
            "Strong alumni network",
            "International standard education",
            "Best starting salaries after graduation"
        ],
        "weaknesses": [
            "Very expensive (Rs. 3.5 Lakh/year)",
            "Extremely competitive — 5% acceptance rate",
            "High pressure environment",
            "Limited financial aid"
        ],
        "environment": "Corporate and professional",
        "campus_life": "Active but study-focused",
        "job_placement": "Excellent",
        "rating": 4.8,
        "merit_2024": {
            "BBA": 88,
            "Computer Science": 85,
            "Economics": 83,
            "Accounting & Finance": 82,
        }
    },
    
    "SZABIST": {
        "full_name": "Shaheed Zulfikar Ali Bhutto Institute of Science and Technology",
        "type": "Private",
        "location": "Clifton, Karachi",
        "established": 1995,
        "website": "www.szabist.edu.pk",
        "phone": "021-111-922-478",
        "fields": ["Computer Science", "Business", "Media Sciences", "Engineering"],
        "programs": ["BS Computer Science", "BBA", "BS Software Engineering",
                    "BS Media Sciences", "BS Electrical Engineering",
                    "BS Accounting & Finance", "BS Artificial Intelligence"],
        "entry_test": "SZABIST Entry Test",
        "test_marks": 100,
        "merit_formula": "Inter 40% + Entry Test 40% + Interview 20%",
        "min_inter_marks": 55,
        "annual_fee": 180000,
        "ranking": 3,
        "strengths": [
            "Modern curriculum",
            "Good IT infrastructure",
            "Industry relevant programs",
            "Active student societies",
            "Good internship opportunities"
        ],
        "weaknesses": [
            "Expensive compared to public universities",
            "Less research focused",
            "Limited campus facilities"
        ],
        "environment": "Modern and industry-focused",
        "campus_life": "Very Active",
        "job_placement": "Very Good",
        "rating": 4.0,
        "merit_2024": {
            "Computer Science": 65,
            "BBA": 60,
            "Software Engineering": 63,
            "Artificial Intelligence": 68,
            "Media Sciences": 58,
        }
    },
    
    "FAST_NUCES": {
        "full_name": "FAST National University of Computer and Emerging Sciences",
        "type": "Private",
        "location": "Stadium Road, Karachi",
        "established": 2000,
        "website": "www.nu.edu.pk",
        "phone": "021-34301891",
        "fields": ["Computer Science", "Engineering", "Business"],
        "programs": ["BS Computer Science", "BS Software Engineering",
                    "BS Artificial Intelligence", "BS Data Science",
                    "BS Electrical Engineering", "BS Civil Engineering",
                    "BBA", "BS Accounting & Finance"],
        "entry_test": "FAST Entry Test (NU-FAST)",
        "test_marks": 100,
        "merit_formula": "Inter 30% + FAST Test 60% + Interview 10%",
        "min_inter_marks": 60,
        "annual_fee": 220000,
        "ranking": 2,
        "strengths": [
            "Best CS university in Karachi (private)",
            "Strong programming culture",
            "Excellent faculty for CS/IT",
            "Good industry connections",
            "Active coding competitions",
            "Strong alumni in tech companies"
        ],
        "weaknesses": [
            "High fee structure",
            "Very tough academic environment",
            "Limited programs outside CS/Engineering"
        ],
        "environment": "Tech-focused, competitive",
        "campus_life": "Active",
        "job_placement": "Excellent",
        "rating": 4.3,
        "merit_2024": {
            "Computer Science": 78,
            "Software Engineering": 75,
            "Artificial Intelligence": 80,
            "Data Science": 72,
            "Electrical Engineering": 70,
        }
    },
    
    "BAHRIA": {
        "full_name": "Bahria University Karachi Campus",
        "type": "Private",
        "location": "Clifton, Karachi",
        "established": 2002,
        "website": "www.bahria.edu.pk",
        "phone": "021-35349154",
        "fields": ["Engineering", "Business", "Computer Science", "Law", "Health Sciences"],
        "programs": ["BS Computer Science", "BS Software Engineering",
                    "BBA", "BS Electrical Engineering", "BS Civil Engineering",
                    "BS Cyber Security", "BS Data Science", "LLB",
                    "BS Health Sciences"],
        "entry_test": "Bahria University Entry Test",
        "test_marks": 100,
        "merit_formula": "Inter 40% + Entry Test 50% + Interview 10%",
        "min_inter_marks": 50,
        "annual_fee": 180000,
        "ranking": 4,
        "strengths": [
            "Military discipline and environment",
            "Good infrastructure",
            "Wide range of programs",
            "Decent industry connections",
            "Safe and disciplined campus"
        ],
        "weaknesses": [
            "Strict rules (some students find it too strict)",
            "Less research culture",
            "Average faculty in some departments"
        ],
        "environment": "Disciplined, military-style",
        "campus_life": "Moderate",
        "job_placement": "Good",
        "rating": 3.7,
        "merit_2024": {
            "Computer Science": 60,
            "Software Engineering": 58,
            "BBA": 55,
            "Electrical Engineering": 57,
            "Cyber Security": 62,
        }
    },
    
    "PAF_KIET": {
        "full_name": "PAF-Karachi Institute of Economics and Technology",
        "type": "Private",
        "location": "Korangi Creek, Karachi",
        "established": 1995,
        "website": "www.pafkiet.edu.pk",
        "phone": "021-35091300",
        "fields": ["Engineering", "Computer Science", "Business", "Sciences"],
        "programs": ["BS Computer Science", "BS Software Engineering",
                    "BS Electrical Engineering", "BS Mechanical Engineering",
                    "BBA", "BS Accounting & Finance", "BS Mathematics"],
        "entry_test": "PAF-KIET Entry Test",
        "test_marks": 100,
        "merit_formula": "Inter 40% + Entry Test 50% + Interview 10%",
        "min_inter_marks": 50,
        "annual_fee": 200000,
        "ranking": 5,
        "strengths": [
            "PAF affiliated — good discipline",
            "Affordable compared to other private universities",
            "Good engineering programs",
            "Peaceful campus environment",
            "Good faculty"
        ],
        "weaknesses": [
            "Less known internationally",
            "Limited extracurricular",
            "Less corporate exposure"
        ],
        "environment": "Disciplined and peaceful",
        "campus_life": "Moderate",
        "job_placement": "Good",
        "rating": 3.6,
        "merit_2024": {
            "Computer Science": 55,
            "Software Engineering": 52,
            "Electrical Engineering": 50,
            "BBA": 48,
        }
    },
    
    "IQRA": {
        "full_name": "Iqra University",
        "type": "Private",
        "location": "Defence View, Karachi",
        "established": 1998,
        "website": "www.iqra.edu.pk",
        "phone": "021-35310584",
        "fields": ["Business", "Computer Science", "Media Sciences", "Education"],
        "programs": ["BBA", "BS Computer Science", "BS Media Sciences",
                    "BS Education", "BS Psychology", "BS Accounting & Finance",
                    "BS Marketing", "BS Human Resource Management"],
        "entry_test": "Iqra University Test",
        "test_marks": 100,
        "merit_formula": "Inter 50% + Entry Test 50%",
        "min_inter_marks": 45,
        "annual_fee": 120000,
        "ranking": 5,
        "strengths": [
            "Good for business programs",
            "Active student life",
            "Good media sciences department",
            "Flexible environment",
            "Good internship network"
        ],
        "weaknesses": [
            "Less research focused",
            "Average CS department",
            "Less recognized by top employers"
        ],
        "environment": "Relaxed and social",
        "campus_life": "Very Active",
        "job_placement": "Average",
        "rating": 3.4,
        "merit_2024": {
            "BBA": 50,
            "Computer Science": 48,
            "Media Sciences": 45,
            "Psychology": 47,
        }
    },
    
    "SMIU": {
        "full_name": "Sindh Madressatul Islam University",
        "type": "Public",
        "location": "Aiwan-e-Tijarat Road, Karachi",
        "established": 2012,
        "website": "www.smiu.edu.pk",
        "phone": "021-99213350",
        "fields": ["Business", "Computer Science", "Social Sciences", "Law"],
        "programs": ["BBA", "BS Computer Science", "BS Software Engineering",
                    "LLB", "BS Economics", "BS Mass Communication",
                    "BS Education", "BS Psychology"],
        "entry_test": "SMIU Entry Test",
        "test_marks": 100,
        "merit_formula": "Inter 50% + Entry Test 50%",
        "min_inter_marks": 45,
        "annual_fee": 75000,
        "ranking": 6,
        "strengths": [
            "Public university — very low fee",
            "Historical building — beautiful campus",
            "Good law program",
            "Growing CS department",
            "Government recognized"
        ],
        "weaknesses": [
            "Newer university — less established",
            "Limited research facilities",
            "Less industry connections"
        ],
        "environment": "Traditional and academic",
        "campus_life": "Moderate",
        "job_placement": "Average",
        "rating": 3.3,
        "merit_2024": {
            "BBA": 52,
            "Computer Science": 50,
            "LLB": 55,
            "Economics": 48,
        }
    }
}

# Merit calculation weights
MERIT_WEIGHTS = {
    "NED": {"matric": 0.10, "inter": 0.40, "test": 0.50},
    "DUET": {"matric": 0.10, "inter": 0.40, "test": 0.50},
    "UBIT_KU": {"matric": 0.00, "inter": 0.50, "test": 0.50},
    "IBA": {"matric": 0.00, "inter": 0.30, "test": 0.50, "interview": 0.20},
    "SZABIST": {"matric": 0.00, "inter": 0.40, "test": 0.40, "interview": 0.20},
    "FAST_NUCES": {"matric": 0.00, "inter": 0.30, "test": 0.60, "interview": 0.10},
    "BAHRIA": {"matric": 0.00, "inter": 0.40, "test": 0.50, "interview": 0.10},
    "PAF_KIET": {"matric": 0.00, "inter": 0.40, "test": 0.50, "interview": 0.10},
    "IQRA": {"matric": 0.00, "inter": 0.50, "test": 0.50},
    "SMIU": {"matric": 0.00, "inter": 0.50, "test": 0.50},
}
