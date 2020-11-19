  movie=Movie.objects.all()
    rating=Rating.objects.all()
    x=[]
    y=[]
    A=[]
    B=[]
    C=[]
    D=[]
    #Movie Data Frames
    for item in movie:
        x=[item.id,item.title,item.year] 
        y+=[x]
    movies_df = pd.DataFrame(y,columns=['movieId','title','year'])
    print("Movies DataFrame")
    print(movies_df)
    #Rating Data Frames
    for item in rating:
        A=[item.user,item.movie,item.rating]
        B+=[A]
    rating_df=pd.DataFrame(B,columns=['userId','movieId','rating'])
    print("Rating data Frame")
    print(rating_df)

    #User Input
    
    userid=request.user.id
    #select related is join statement in django.It looks for foreign key and join the table
    watched_movie_by_user=Rating.objects.select_related('movie').filter(user=userid)
    for item in watched_movie_by_user:
        C=[item.movie.id,item.movie.title,item.rating]
        D+=[C]
    watched_movies_by_user_df=pd.DataFrame(D,columns=['movieId','title','rating'])
    print("Watched Movies by user dataframe")
    print(watched_movies_by_user_df)

    #Filtering out users that have watched movies that the input has watched and storing it
    userSubset = rating_df[rating_df['movieId'].isin(watched_movies_by_user_df['movieId'].tolist())]
    print("User Subset")
    print(userSubset)