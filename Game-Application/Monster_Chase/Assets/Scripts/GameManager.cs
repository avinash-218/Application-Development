using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager instance; // create instance of the class inside the same class (static - only one for all objects)

    [SerializeField]
    private GameObject[] characters;

    private int _charIndex;
    public int CharIndex
    {
        get { return _charIndex; }
        set { _charIndex = value; }
    }

    public void Awake()
    {
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void OnEnable()
    {
        SceneManager.sceneLoaded += onLevelFinishedLoading;
    }

    public void OnDisable()
    {
        SceneManager.sceneLoaded -= onLevelFinishedLoading;
    }

    void onLevelFinishedLoading(Scene scene, LoadSceneMode mode)
    {
        if(scene.name == "Gameplay")
        {
            Instantiate(characters[CharIndex]);
        }
        else
        {

        }
    }

}