def build_profile(first, last, **userprofile):
    userprofile['firstname'] = first
    userprofile['lastname'] = last
    return userprofile