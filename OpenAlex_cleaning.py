import json

# Load JSON from a file
with open("openalex_data2023.json", "r") as file:
    data = json.load(file)

# Remove 'meta'
del data["meta"]


keys_to_drop = {"id","primary_location", "open_access", "biblio","doi","display_name","publication_year","ids","type","type_crossref","indexed_in","institution_assertions",
                "countries_distinct_count","institutions_distinct_count","corresponding_author_ids","corresponding_institution_ids",
                "apc_list","apc_paid","fwci","has_fulltext","citation_normalized_percentile","cited_by_percentile_year","is_retracted",
                "is_paratext","topics","keywords","concepts","mesh","locations_count","locations","best_oa_location",
                "sustainable_development_goals","datasets","versions","referenced_works_count","referenced_works",
                "abstract_inverted_index","cited_by_api_url","counts_by_year","updated_date","created_date","related_works","is_authors_truncated","fulltext_origin"}


# Filter each object in the results list
filtered_results = [
    {key: value for key, value in item.items() if key not in keys_to_drop}
    for item in data["results"]
]

data["results"] = filtered_results

# Save updated JSON back to the file
with open("openalex_data2023.json", "w") as file:
    json.dump(data, file, indent=4)


