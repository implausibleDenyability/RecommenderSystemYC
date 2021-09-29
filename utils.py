import pandas as pd

def convert_ids_to_ordered(users: pd.DataFrame, organizations: pd.DataFrame, reviews: pd.DataFrame) -> tuple:
    ordered_users = users.copy()
    ordered_users['ordered_id'] = range(len(ordered_users)) 
    ordered_organizations = organizations.copy()
    ordered_organizations['ordered_id'] = range(len(ordered_organizations)) 
    ordered_reviews = reviews.join(
        ordered_users[['ordered_id']], on='user_id').join(
        ordered_organizations[['ordered_id']], on='org_id', lsuffix='_user', rsuffix='_org'
    )
    ordered_reviews = ordered_reviews.drop(["user_id", 'org_id'], axis=1)
    return ordered_users, ordered_organizations, ordered_reviews