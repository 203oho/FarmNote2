/* tslint:disable */
/* eslint-disable */
/**
 * FarmNote
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: r206067@fhwn.ac.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import type {
  HTTPError,
  HTTPValidationError,
  Note,
  NoteCreate,
  NoteUpdate,
} from '../models/index';
import {
    HTTPErrorFromJSON,
    HTTPErrorToJSON,
    HTTPValidationErrorFromJSON,
    HTTPValidationErrorToJSON,
    NoteFromJSON,
    NoteToJSON,
    NoteCreateFromJSON,
    NoteCreateToJSON,
    NoteUpdateFromJSON,
    NoteUpdateToJSON,
} from '../models/index';

export interface CreateNoteRequest {
    token: string;
    noteCreate: NoteCreate;
}

export interface DeleteNoteRequest {
    noteId: number;
    token: string;
}

export interface ReadNoteRequest {
    noteId: number;
    token: string;
}

export interface ReadNotesRequest {
    token: string;
}

export interface UpdateNoteRequest {
    noteId: number;
    token: string;
    noteUpdate: NoteUpdate;
}

/**
 *
 */
export class NotesApi extends runtime.BaseAPI {

    /**
     * Creates a new note for an existing session.
     * Create Note
     */
    async createNoteRaw(requestParameters: CreateNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Note>> {
        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling createNote().'
            );
        }

        if (requestParameters['noteCreate'] == null) {
            throw new runtime.RequiredError(
                'noteCreate',
                'Required parameter "noteCreate" was null or undefined when calling createNote().'
            );
        }

        const queryParameters: any = {};

        if (requestParameters['token'] != null) {
            queryParameters['token'] = requestParameters['token'];
        }

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/notes/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: NoteCreateToJSON(requestParameters['noteCreate']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => NoteFromJSON(jsonValue));
    }

    /**
     * Creates a new note for an existing session.
     * Create Note
     */
    async createNote(requestParameters: CreateNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Note> {
        const response = await this.createNoteRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Deletes an existing note.
     * Delete Note
     */
    async deleteNoteRaw(requestParameters: DeleteNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Note>> {
        if (requestParameters['noteId'] == null) {
            throw new runtime.RequiredError(
                'noteId',
                'Required parameter "noteId" was null or undefined when calling deleteNote().'
            );
        }

        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling deleteNote().'
            );
        }

        const queryParameters: any = {};

        if (requestParameters['token'] != null) {
            queryParameters['token'] = requestParameters['token'];
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/notes/{note_id}`.replace(`{${"note_id"}}`, encodeURIComponent(String(requestParameters['noteId']))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => NoteFromJSON(jsonValue));
    }

    /**
     * Deletes an existing note.
     * Delete Note
     */
    async deleteNote(requestParameters: DeleteNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Note> {
        const response = await this.deleteNoteRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Return a specific note.
     * Read Note
     */
    async readNoteRaw(requestParameters: ReadNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Note>> {
        if (requestParameters['noteId'] == null) {
            throw new runtime.RequiredError(
                'noteId',
                'Required parameter "noteId" was null or undefined when calling readNote().'
            );
        }

        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling readNote().'
            );
        }

        const queryParameters: any = {};

        if (requestParameters['token'] != null) {
            queryParameters['token'] = requestParameters['token'];
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/notes/{note_id}`.replace(`{${"note_id"}}`, encodeURIComponent(String(requestParameters['noteId']))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => NoteFromJSON(jsonValue));
    }

    /**
     * Return a specific note.
     * Read Note
     */
    async readNote(requestParameters: ReadNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Note> {
        const response = await this.readNoteRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Return all note of an existing session.
     * Read Notes
     */
    async readNotesRaw(requestParameters: ReadNotesRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Array<Note>>> {
        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling readNotes().'
            );
        }

        const queryParameters: any = {};

        if (requestParameters['token'] != null) {
            queryParameters['token'] = requestParameters['token'];
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/notes/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);


        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(NoteFromJSON));
    }

    /**
     * Return all note of an existing session.
     * Read Notes
     */
    async readNotes(requestParameters: ReadNotesRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Array<Note>> {
        const response = await this.readNotesRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Changes an existing note.
     * Update Note
     */
    async updateNoteRaw(requestParameters: UpdateNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Note>> {
        if (requestParameters['noteId'] == null) {
            throw new runtime.RequiredError(
                'noteId',
                'Required parameter "noteId" was null or undefined when calling updateNote().'
            );
        }

        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling updateNote().'
            );
        }

        if (requestParameters['noteUpdate'] == null) {
            throw new runtime.RequiredError(
                'noteUpdate',
                'Required parameter "noteUpdate" was null or undefined when calling updateNote().'
            );
        }

        const queryParameters: any = {};

        if (requestParameters['token'] != null) {
            queryParameters['token'] = requestParameters['token'];
        }

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/notes/{note_id}`.replace(`{${"note_id"}}`, encodeURIComponent(String(requestParameters['noteId']))),
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: NoteUpdateToJSON(requestParameters['noteUpdate']),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => NoteFromJSON(jsonValue));
    }

    /**
     * Changes an existing note.
     * Update Note
     */
    async updateNote(requestParameters: UpdateNoteRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Note> {
        const response = await this.updateNoteRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
