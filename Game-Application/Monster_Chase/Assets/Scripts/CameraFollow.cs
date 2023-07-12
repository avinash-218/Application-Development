using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraFollow : MonoBehaviour
{

    private Transform player;
    private Vector3 tempPos;

    [SerializeField]
    private float minX, maxX;

    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.FindWithTag("Player").transform;
    }

    void LateUpdate() // Called once per frame after all calculations in update()
    {
        if(player == null)
        {
            return;
        }
        tempPos = transform.position;
        tempPos.x = player.position.x;

        if(tempPos.x < minX)
        {
            tempPos.x = minX;
        }
        else if(tempPos.x > maxX)
        {
            tempPos.x = maxX;
        }

        transform.position = tempPos;
    }
}