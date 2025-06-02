import os
from collections import defaultdict
import re
import argparse

def analyze_description(text):
    # Convert to lowercase for case-insensitive matching
    text = text.lower()
    
    # Initialize categories
    categories = {
        'day': False,
        'night': False,
        'rainy': False,
        'cloudy': False,
        'sunny': False,
        'foggy': False
    }
    
    # Time of day patterns
    if re.search(r'\b(day|daylight|sunlight|bright|sunny day)\b', text) and not re.search(r'\b(no day|not day)\b', text):
        categories['day'] = True
    if re.search(r'\b(night|dark|evening|dusk|dawn|sunset|sunrise)\b', text) and not re.search(r'\b(no night|not night)\b', text):
        categories['night'] = True
    
    # Weather patterns
    if re.search(r'\b(rain|raining|rainy|drizzle|drizzling|wet|shower)\b', text) and not re.search(r'\b(no rain|not raining)\b', text):
        categories['rainy'] = True
    if re.search(r'\b(cloud|clouds|cloudy|overcast)\b', text) and not re.search(r'\b(no cloud|clear sky|clear skies)\b', text):
        categories['cloudy'] = True
    if re.search(r'\b(sun|sunny|clear|bright)\b', text) and not re.search(r'\b(no sun|not sunny)\b', text):
        categories['sunny'] = True
    if re.search(r'\b(fog|foggy|mist|misty|haze|hazy)\b', text) and not re.search(r'\b(no fog|not foggy)\b', text):
        categories['foggy'] = True
    
    return categories

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Categorize dashcam footage descriptions based on weather and time conditions.')
    parser.add_argument('-d', '--directory', required=True, help='Directory path containing the footage description files')
    args = parser.parse_args()
    
    # Initialize counters
    category_counts = defaultdict(int)
    total_files = 0
    
    # Process each .txt file in the directory
    for filename in os.listdir(args.directory):
        if filename.endswith('.txt'):
            total_files += 1
            file_path = os.path.join(args.directory, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    categories = analyze_description(content)
                    
                    # Update category counts
                    for category, is_present in categories.items():
                        if is_present:
                            category_counts[category] += 1
                            
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    
    # Print results
    print("\nFootage Categorization Results:")
    print("-" * 30)
    print(f"Total files processed: {total_files}")
    print("\nCategory counts:")
    for category, count in category_counts.items():
        print(f"{category.capitalize()}: {count} videos")

if __name__ == "__main__":
    main() 