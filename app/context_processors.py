def active_paths(request):
    return {
        'donation_active_paths': [
            '/admin-panel/pending-donation/',
            '/admin-panel/accepted-donation/',
            '/admin-panel/rejected-donation/',
            '/admin-panel/volunteerallocated-donation/',
            '/admin-panel/donationrec-admin/',
            '/admin-panel/donationnotrec-admin/',
            '/admin-panel/donationdelivered-admin/',
            '/admin-panel/all-donations/',
        ],
        'area_active_paths': [
            '/admin-panel/add-area/',
            '/admin-panel/manage-area/',
        ],

        'volunteer_active_paths': [
            '/admin-panel/new-volunteer/',
            '/admin-panel/accepted-volunteer/',
            '/admin-panel/rejected-volunteer/',
            '/admin-panel/all-volunteer/',
        ],
        'collection_history_active_paths':[
            '/volunteer/donation-list/donationrec-volunteer/',
            '/volunteer/donation-list/donationnotrec-volunteer/',
            '/volunteer/donation-list/donationdelivered-volunteer/',
        ]

        
    }
