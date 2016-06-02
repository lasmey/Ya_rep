import pickle

TREE={
    'name': 'body',
    'elements':[
        {
        'name':'Head',
        'elements':[
            {
            'name': 'Eyes'},
    ]},
    {
            'name': 'Arm'
        }
    ]
}

pickle.dump(TREE, open('read_write.data','wb'))


