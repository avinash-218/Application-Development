using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    [SerializeField] //make it private to but can be accessed in unity
    private float moveForce = 10f;
    [SerializeField]
    private float jumpForce = 11f;

    private float movementX;

    private Rigidbody2D myBody;
    private SpriteRenderer sr;
    private Animator anim;
    private string WALK_ANIMATION = "Walk";
    private string GROUND_TAG = "Ground";
    private string ENEMY_TAG = "Enemy";

    private bool isGrounded = false;

    private void Awake()
    {
        myBody = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        sr = GetComponent<SpriteRenderer>();
    }


    // Start is called before the first frame update
    void Start()
    {
        
    }

    void Update() // Update is called once per frame
    {
        PlayerMoveKeyboard();
        AnimatePlayer();
        PlayerJump();
    }

    private void FixedUpdate() // Called every fixed number of time
    {
        
    }

    void PlayerMoveKeyboard()
    {
        movementX = Input.GetAxisRaw("Horizontal");
        transform.position += new Vector3(movementX, 0f, 0f) * Time.deltaTime * moveForce;
    }

    void AnimatePlayer()
    {

        if(movementX > 0)
        {
            anim.SetBool(WALK_ANIMATION, true);
            sr.flipX = false;
        }
        else if(movementX < 0)
        {
            anim.SetBool(WALK_ANIMATION, true);
            sr.flipX = true;
        }
        else
        {
            anim.SetBool(WALK_ANIMATION, false);
        }
    }

    void PlayerJump()
    {
        if(Input.GetButtonDown("Jump") && isGrounded)
        {
            isGrounded = false;
            myBody.AddForce(new Vector2(0f, jumpForce), ForceMode2D.Impulse);
        }
    }

    private void onCollisionEnter2D(Collision2D collision) //inbuilt function to detect if two object collided
    {
        if(collision.gameObject.CompareTag(GROUND_TAG))
        {
            isGrounded = true;
            Debug.Log("Touched Ground");
        }
    }

    private void onTriggerEnter2D(Collider2D collision) //inbuilt function to detect if two object collided
    {
        if (collision.CompareTag(ENEMY_TAG))
        {
            Destroy(gameObject);
            Debug.Log("Touched enemy");
        }
    }
}
