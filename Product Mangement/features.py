import csv
import json
import datetime
import random
import os
from collections import defaultdict


class CustomerSatisfactionAnalyzer:
    def __init__(self, data_file=None):
        """Initialize the customer satisfaction analyzer."""
        self.data = []
        self.results = {}
        
        if data_file and os.path.exists(data_file):
            self.load_data(data_file)
            
    def load_data(self, data_file):
        """Load survey data from a CSV file."""
        try:
            with open(data_file, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
                
            # Convert satisfaction scores to integers
            for row in self.data:
                if 'satisfaction_score' in row:
                    try:
                        row['satisfaction_score'] = int(row['satisfaction_score'])
                    except ValueError:
                        pass  # Keep as string if conversion fails
                        
            print(f"Loaded {len(self.data)} survey responses from {data_file}")
            return self.data
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
            
    def create_sample_data(self, num_samples=100, categories=None, save_to_file=True):
        """Create sample survey data for testing."""
        if categories is None:
            categories = ['Product', 'Customer Service', 'Website', 'App']
            
        self.data = []
        today = datetime.date.today()
        
        for i in range(1, num_samples + 1):
            # Generate a random date within the last 90 days
            random_days = random.randint(0, 90)
            survey_date = today - datetime.timedelta(days=random_days)
            
            # Generate random satisfaction score (1-5)
            # Weighted toward higher scores for realism
            score = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.1, 0.2, 0.35, 0.3])[0]
            
            # Select random category
            category = random.choice(categories)
            
            # Generate a simple comment based on the score
            if score >= 4:
                comment = f"Satisfied with the {category.lower()}. Works great!"
            elif score == 3:
                comment = f"The {category.lower()} is okay, but could be improved."
            else:
                comment = f"Disappointed with the {category.lower()}. Needs significant improvements."
            
            # Create survey response
            survey_response = {
                'customer_id': f"CUST_{i:04d}",
                'date': survey_date.strftime('%Y-%m-%d'),
                'category': category,
                'satisfaction_score': score,
                'comments': comment
            }
            
            self.data.append(survey_response)
        
        if save_to_file:
            filename = f"sample_satisfaction_data.csv"
            self._save_to_csv(filename, self.data)
            print(f"Sample data with {num_samples} responses saved to {filename}")
            
        return self.data
    
    def _save_to_csv(self, filename, data):
        """Helper method to save data to CSV."""
        if not data:
            return
            
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    def calculate_csat(self):
        """Calculate Customer Satisfaction Score (CSAT) as percentage of satisfied customers."""
        if not self.data:
            print("No data available for CSAT calculation.")
            return 0.0
        
        # Count responses with scores of 4 or 5 (satisfied or very satisfied)
        satisfied_responses = sum(1 for row in self.data 
                                if row.get('satisfaction_score', 0) >= 4)
        total_responses = len(self.data)
        
        csat_percentage = (satisfied_responses / total_responses) * 100 if total_responses > 0 else 0
        self.results['csat_percentage'] = csat_percentage
        
        print(f"CSAT Score: {csat_percentage:.2f}%")
        print(f"Based on {satisfied_responses} satisfied responses out of {total_responses} total")
        
        return csat_percentage
        
    def calculate_composite_csat(self):
        """Calculate composite CSAT (average score)."""
        if not self.data:
            print("No data available for composite CSAT calculation.")
            return 0.0
        
        # Calculate average satisfaction score
        total_score = sum(row.get('satisfaction_score', 0) for row in self.data)
        total_responses = len(self.data)
        
        composite_score = total_score / total_responses if total_responses > 0 else 0
        self.results['composite_csat'] = composite_score
        
        print(f"Composite CSAT Score: {composite_score:.2f} / 5.00")
        
        return composite_score
    
    def analyze_by_category(self):
        """Analyze satisfaction scores by category."""
        if not self.data:
            print("No data available for category analysis.")
            return {}
        
        # Group data by category
        categories = {}
        for row in self.data:
            category = row.get('category')
            score = row.get('satisfaction_score', 0)
            
            if category not in categories:
                categories[category] = {'scores': [], 'count': 0}
                
            categories[category]['scores'].append(score)
            categories[category]['count'] += 1
        
        # Calculate metrics for each category
        category_results = {}
        for category, data in categories.items():
            scores = data['scores']
            total = data['count']
            
            # Calculate CSAT percentage
            satisfied = sum(1 for score in scores if score >= 4)
            csat_percentage = (satisfied / total) * 100 if total > 0 else 0
            
            # Calculate composite score
            composite_score = sum(scores) / total if total > 0 else 0
            
            category_results[category] = {
                'csat_percentage': csat_percentage,
                'composite_score': composite_score,
                'sample_size': total
            }
            
            print(f"\nCategory: {category}")
            print(f"  CSAT: {csat_percentage:.2f}%")
            print(f"  Composite Score: {composite_score:.2f} / 5.00")
            print(f"  Sample Size: {total}")
        
        self.results['category_analysis'] = category_results
        return category_results
    
    def identify_unhappy_customers(self, threshold=3):
        """Identify customers who provided low satisfaction scores."""
        if not self.data:
            print("No data available for unhappy customer identification.")
            return []
        
        unhappy_customers = [row for row in self.data 
                           if row.get('satisfaction_score', 0) <= threshold]
        
        if unhappy_customers:
            print(f"\nIdentified {len(unhappy_customers)} unhappy customers (score <= {threshold})")
            self.results['unhappy_customers'] = unhappy_customers
            
            # Display first few unhappy customers
            for i, customer in enumerate(unhappy_customers[:5]):
                print(f"{i+1}. Customer ID: {customer.get('customer_id')}, "
                      f"Score: {customer.get('satisfaction_score')}, "
                      f"Category: {customer.get('category')}")
                
            if len(unhappy_customers) > 5:
                print(f"... and {len(unhappy_customers) - 5} more")
                
            return unhappy_customers
        else:
            print("No unhappy customers identified.")
            return []
    
    def analyze_trends(self, freq='weekly'):
        """Analyze satisfaction score trends over time."""
        if not self.data:
            print("No data available for trend analysis.")
            return {}
        
        # Convert date strings to datetime objects
        for row in self.data:
            if 'date' in row and isinstance(row['date'], str):
                try:
                    row['date_obj'] = datetime.datetime.strptime(row['date'], '%Y-%m-%d').date()
                except ValueError:
                    # Skip rows with invalid dates
                    row['date_obj'] = None
        
        # Filter out rows with invalid dates
        valid_data = [row for row in self.data if row.get('date_obj')]
        
        if not valid_data:
            print("No valid dates found in data for trend analysis.")
            return {}
        
        # Group data by time period
        periods = {}
        for row in valid_data:
            date_obj = row['date_obj']
            score = row.get('satisfaction_score', 0)
            
            # Determine period key based on frequency
            if freq == 'daily':
                period_key = date_obj.strftime('%Y-%m-%d')
            elif freq == 'weekly':
                # Get the Monday of the week
                monday = date_obj - datetime.timedelta(days=date_obj.weekday())
                period_key = monday.strftime('%Y-%m-%d')
            elif freq == 'monthly':
                period_key = date_obj.strftime('%Y-%m')
            else:
                # Default to weekly
                monday = date_obj - datetime.timedelta(days=date_obj.weekday())
                period_key = monday.strftime('%Y-%m-%d')
            
            if period_key not in periods:
                periods[period_key] = {'scores': [], 'count': 0}
                
            periods[period_key]['scores'].append(score)
            periods[period_key]['count'] += 1
        
        # Calculate metrics for each period
        trend_results = {}
        for period_key, data in sorted(periods.items()):
            scores = data['scores']
            total = data['count']
            
            # Calculate average score
            avg_score = sum(scores) / total if total > 0 else 0
            
            # Calculate CSAT percentage
            satisfied = sum(1 for score in scores if score >= 4)
            csat_percentage = (satisfied / total) * 100 if total > 0 else 0
            
            trend_results[period_key] = {
                'avg_score': avg_score,
                'csat_percentage': csat_percentage,
                'response_count': total
            }
        
        self.results['trends'] = trend_results
        
        print(f"\nSatisfaction Trends ({freq}):")
        for period, metrics in sorted(trend_results.items()):
            print(f"  {period}: CSAT {metrics['csat_percentage']:.2f}%, "
                  f"Avg Score {metrics['avg_score']:.2f}, "
                  f"Responses {metrics['response_count']}")
        
        return trend_results
        
    def export_results(self, output_file="satisfaction_analysis.json"):
        """Export analysis results to a JSON file."""
        if not self.results:
            print("No results available to export.")
            return
        
        # Prepare results for export
        export_data = {
            'summary': {
                'csat_percentage': self.results.get('csat_percentage', 0),
                'composite_csat': self.results.get('composite_csat', 0),
                'total_responses': len(self.data) if self.data else 0,
                'analysis_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        }
        
        # Add category analysis if available
        if 'category_analysis' in self.results:
            export_data['category_analysis'] = self.results['category_analysis']
        
        # Add unhappy customers if available
        if 'unhappy_customers' in self.results:
            export_data['unhappy_customers'] = self.results['unhappy_customers']
        
        # Add trends if available
        if 'trends' in self.results:
            export_data['trends'] = self.results['trends']
        
        # Export to JSON
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(export_data, file, indent=2)
            print(f"\nResults exported to {output_file}")
        except Exception as e:
            print(f"Error exporting results: {e}")


def main():
    """Main function to run the customer satisfaction analysis."""
    print("Customer Satisfaction Analysis Tool")
    print("==================================")
    
    # Get user input for action
    print("\nWhat would you like to do?")
    print("1. Load existing survey data")
    print("2. Generate sample data")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    analyzer = CustomerSatisfactionAnalyzer()
    
    if choice == '1':
        file_path = input("Enter the path to your CSV file: ")
        analyzer.load_data(file_path)
    elif choice == '2':
        try:
            num_samples = int(input("How many sample responses to generate? (default: 100): ") or 100)
            categories_input = input("Enter categories, comma-separated (default: Product,Service,Website,App): ")
            categories = [c.strip() for c in categories_input.split(',')] if categories_input else None
            analyzer.create_sample_data(num_samples=num_samples, categories=categories)
        except ValueError:
            print("Invalid number, using default of 100 samples")
            analyzer.create_sample_data()
    else:
        print("Exiting program.")
        return
    
    # If we have data, run analysis
    if analyzer.data:
        # Run all analyses
        analyzer.calculate_csat()
        analyzer.calculate_composite_csat()
        analyzer.analyze_by_category()
        analyzer.identify_unhappy_customers()
        analyzer.analyze_trends()
        
        # Ask about exporting results
        export_choice = input("\nWould you like to export the results? (y/n): ")
        if export_choice.lower() == 'y':
            output_file = input("Enter output file name (default: satisfaction_analysis.json): ") or "satisfaction_analysis.json"
            analyzer.export_results(output_file)
        
        print("\nAnalysis complete!")
    else:
        print("\nNo data available for analysis.")


if __name__ == "__main__":
    main()