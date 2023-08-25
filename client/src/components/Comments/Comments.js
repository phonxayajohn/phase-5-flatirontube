import React from 'react'

const Comments = () => {
    const handleComment = () => { }

    return (
        <div className='comments'>
            <p>Comments</p>
            <div className='comments_form'>
                <form onSubmit={handleComment}>
                    <input type="text" placeholder="Write a comment..." />
                    <button className="comments_button">Comment</button>
                </form>
            </div>
        </div>
    )
}

export default Comments