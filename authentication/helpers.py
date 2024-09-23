
def validate_users_access(request, groups = []):
    for group in groups:
        if group not in request.user.groups.values_list('name', flat=True):
            return True
    return False