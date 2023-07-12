using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Monster : MonoBehaviour
{
    [HideInInspector]
    public float speed;

    private Rigidbody2D myBody;

    void Awake()
    {
        myBody = GetComponent<Rigidbody2D>();
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    void FixedUpdate() //
    {
        myBody.velocity = new Vector2(speed, myBody.velocity.y); //add velocity to x axis alone; set same to y axis
    }
}
