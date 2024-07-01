import { useEffect, useState } from 'react'
import './App.css'

function App() {
    const [posts, setPosts] = useState([]);
    let title, description, comment = '';

    useEffect(() => {
        (async () => {
            const response = await fetch('http://127.0.0.1:8000/api/posts/');

            const content = await response.json()

            setPosts(content);
        })()
    }, []);

    const createPost = async e => {
        e.preventDefault();

        const res = await fetch('http://127.0.0.1:8000/api/posts/', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                description,
            })
        });

        const createdPost = await res.json();

        setPosts([...posts, createdPost]);
    }

    const createComment = async (e, post_id) => {
        e.preventDefault();

        const response = await fetch('http://127.0.0.1:8001/api/comments/', {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                post_id,
                text: comment
            })
        });

        const createdComment = await response.json();

        comment = ''

        setPosts(posts.map(p => {
            if (p.id === post_id) {
                p.comments.push(createdComment)
            }

            return p;
        }))
    }
    return (
        <div className="App container">
            <form className="row my-5" onSubmit={createPost}>
                <div className="col-4">
                    <h2>Create a Post</h2>

                    <input className="form-control mb-4" onChange={e => title = e.target.value}/> <br />
                    <textarea className="form-control mb-3" onChange={e => description = e.target.value}/> <br />

                    <button className="btn btn-primary" type="submit">Save</button>
                </div>
            </form>

            <main>
                <div className="row row-cols-1 row-cols-md-3 mb-3 text-center">
                    {posts.length && posts.map(
                        post => {
                            return (
                                <div className="col" key={post.id}>
                                    <div className="card mb-4 rounded-3 shadow-sm">
                                        <div className="card-header py-3">
                                            <h4 className="my-0 fw-normal">{post.title}</h4>
                                        </div>
                                        <div className="card-body">
                                            <p className="card-title pricing-card-title">{post.description}</p>
                                            <form onSubmit={e => createComment(e, post.id)}>
                                                <input className="w-100 form-control"
                                                       onChange={e => comment = e.target.value}/> <br />

                                                <button className="btn btn-primary" type="submit">Save</button>
                                            </form>
                                        </div>
                                        {post.comments && post.comments.map(
                                            comment => {
                                                return (
                                                    <div className="card-footer py-3" key={comment.id}>
                                                        {comment.text}
                                                    </div>
                                                )
                                            }
                                        )}
                                    </div>
                                </div>
                            )
                        }
                    )}
                </div>
            </main>
        </div>
    );
}

export default App;


// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vitejs.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.jsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App
